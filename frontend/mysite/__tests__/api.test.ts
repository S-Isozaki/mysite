import { expect, jest, test } from "@jest/globals";
import axios from 'axios';

export const fetchData = async () => {
    const response = await axios.get('https://example.com/data');
    return response.data;
};

jest.mock('axios');
const axiosMock = axios as jest.Mocked<typeof axios>;

test('fetches data successfully from an API', async () => {
    const mockData = { data: 'some data' };
    axiosMock.get.mockResolvedValue(mockData);

    const result = await fetchData();

    expect(result).toEqual(mockData.data);
});